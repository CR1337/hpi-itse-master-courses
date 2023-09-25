from typing import List


class Course:

    CATEGORIES: List[str] = [
        "HPI-ITSE-A",
        "HPI-ITSE-E",
        "HPI-ITSE-K",
        "HPI-ITSE-M",
        "HPI-ITSE-MK",
        "HPI-BPET-K",
        "HPI-BPET-T",
        "HPI-BPET-S",
        "HPI-HCGT-K",
        "HPI-HCGT-T",
        "HPI-HCGT-S",
        "HPI-ISAE-K",
        "HPI-ISAE-T",
        "HPI-ISAE-S",
        "HPI-OSIS-K",
        "HPI-OSIS-T",
        "HPI-OSIS-S",
        "HPI-SAMT-K",
        "HPI-SAMT-T",
        "HPI-SAMT-S",
        "HPI-PSK-RW",
        "HPI-PSK-KO",
        "HPI-PSK-DTB",
        "HPI-PSK-DTA"
    ]

    sws: int
    ects: int
    title: str
    type_: str
    mandatory: bool
    language: str
    categories: List[str]

    def __init__(self):
        self.sws = None
        self.ects = None
        self.title = None
        self.type_ = None
        self.mandatory = None
        self.language = None
        self.categories = []

    def __str__(self) -> str:
        return (
            "Course(\n"
            f"    title={self.title},\n"
            f"    sws={self.sws},\n"
            f"    ects={self.ects},\n"
            f"    type_={self.type_},\n"
            f"    mandatory={self.mandatory},\n"
            f"    language={self.language},\n"
            f"    categories={self.categories}\n"
            ")"
        )
