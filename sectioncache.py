from typing import Dict
from section import Section

class SectionCache:
    Sections: Dict[str, Section] = {}

    @staticmethod
    def get_Section(name: str, description: str) -> Section:
        Section = SectionCache.Sections.get(name)

        if Section is None:
            Section = Section(name, description)
            SectionCache.Sections[name] = Section

        return Section
