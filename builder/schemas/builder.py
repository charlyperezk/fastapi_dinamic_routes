from builder.schemas.field import Field


class BuilderScheme:
    def get_fields(self) -> tuple[Field]:
        fields = ()
        for tup in vars(self).items():
            if tup[0].startswith("__") and tup[0].endswith("__"):
                continue
            else:
                tup[1]._name=tup[0]
                fields += (tup[1],)
        return fields