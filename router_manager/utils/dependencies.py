from router_manager.utils.entity import Entity
from router_manager.utils.supervisor import Supervisor
from router_manager.utils import exceptions as exc
from router_manager.db import CRUDController
from sqlalchemy.orm import Session
from fastapi import APIRouter


class DependenciesSupervisor:

    """ 
    This class is responsible for managing dependencies between components.
    It is used to analyze dependencies between components and to manage the
    addition and removal of dependencies.
    """

    def __init__(self):
        self.dependencies = {
            "router": None,
            "session": None,
            "entity": None,
            "supervisor": None,
            "crud": None
        }	

    def supervise_instancies(self, *args, **kwargs):

        dependencies = {}	

        for tuple in args:
            for value in tuple:
                if not any([isinstance(value, Session), isinstance(value, Entity), isinstance(value, Supervisor), isinstance(value, CRUDController)]):
                    raise exc.InvalidDependency("Invalid dependency type")                
                if isinstance(value, APIRouter):
                    dependencies["router"] = value
                if isinstance(value, Entity):
                    dependencies["entity"] = value
                if isinstance(value, Supervisor):
                    dependencies["supervisor"] = value
                if isinstance(value, Session):
                    dependencies["session"] = value
                if isinstance(value, CRUDController):
                    dependencies["crud"] = value

        return dependencies
        
    def set_atributes(self, dependencies):
        for key, value in dependencies.items():
            setattr(self, key, value)
        # for key, value in self.dependencies.items():
            # if not hasattr(self, key):
                # raise utils.exc.MissingDependency(f"Missing {key} dependency")
        if not hasattr(self, "entity"):
            raise exc.MissingDependency("Missing entity dependency")
        if not hasattr(self, "supervisor"):
            self.supervisor = Supervisor()
        if not hasattr(self, "session"):
            raise exc.MissingDependency("Missing session dependency")
        if not hasattr(self, "crud"):
            raise exc.MissingDependency("Missing crud dependency")

    def analyze_dependencies(self, *args, **kwargs):
        try:
            dependencies = self.supervise_instancies(*args, **kwargs)
            self.set_atributes(dependencies)
        
        except Exception as e:
            raise exc.InitializationError(f"Error analyzing dependencies. Message: {e}")

    def add_dependency(self, component, dependency):
        if component in self.dependencies:
            self.dependencies[component].append(dependency)
        else:
            self.dependencies[component] = [dependency]

    def get_dependencies(self, component):
        if component in self.dependencies:
            return self.dependencies[component]
        return []

    def get_all_dependencies(self, component):
        dependencies = self.get_dependencies(component)
        for dependency in dependencies:
            dependencies.extend(self.get_all_dependencies(dependency))
        return dependencies

    def get_all_dependents(self, component):
        dependents = []
        for key, value in self.dependencies.items():
            if component in value:
                dependents.append(key)
        return dependents

    def remove_dependency(self, component, dependency):
        if component in self.dependencies:
            self.dependencies[component].remove(dependency)
        if dependency in self.dependencies:
            self.dependencies[dependency].remove(component)

    def remove_component(self, component):
        if component in self.dependencies:
            del self.dependencies[component]
        for key, value in self.dependencies.items():
            if component in value:
                value.remove(component)

    def get_all_components(self):
        return list(self.dependencies.keys())