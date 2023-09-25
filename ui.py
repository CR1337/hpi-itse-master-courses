from pathvalidate import validate_filename, ValidationError


class Ui:

    @classmethod
    def ask_filename(cls, default_extension: str = None) -> str:
        filename = input("Filename> ")
        while True:
            try:
                validate_filename(filename)
            except ValidationError as e:
                print(f"Invalid filename: {e}")
                filename = input("Filename> ")
            else:
                break
        if (
            default_extension is not None
            and not filename.endswith(default_extension)
        ):
            filename += default_extension
        return filename
