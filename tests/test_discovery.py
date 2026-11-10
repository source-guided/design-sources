"""원천 소유의 대표 독자 질문으로 실제 참조 검색과 후속 주소 해석을 검증한다."""

from pathlib import Path
import unittest

from reference_catalog import Catalog
from reference_io import load_index

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    ('접근성', 'accessibility-criteria'),
    ('accessibility', 'accessibility-criteria'),
    ('키보드', 'accessibility-criteria'),
    ('keyboard', 'accessibility-criteria'),
    ('오류 복구', 'feedback-criteria'),
    ('feedback', 'feedback-criteria'),
    ('화면 설계', 'context-criteria'),
    ('사용자 흐름', 'context-criteria'),
    ('시각적 표현', 'visual-criteria'),
    ('visual hierarchy', 'visual-criteria'),
    ('레이아웃 시프트', 'state-continuity'),
]


class DiscoveryTest(unittest.TestCase):
    def test_reader_questions_find_relevant_sources(self):
        catalog = Catalog(load_index)
        for query, identifier in CASES:
            with self.subTest(query=query):
                found = catalog.discover([ROOT / "references/index.json"], query, limit=5)
                self.assertTrue(found["complete"], found["errors"])
                matches = [item for item in found["references"] if item["reference"]["id"] == identifier]
                self.assertTrue(matches, f"{query!r} did not find {identifier!r} in the first five results")
                reference = matches[0]["reference"]
                resolved = catalog.resolve(reference["index"], identifier, access=reference["access"])
                self.assertEqual(resolved["address"], matches[0]["address"])
                self.assertTrue(Path(resolved["address"]).is_relative_to(ROOT))
                self.assertTrue(Path(resolved["address"]).is_file())

    def test_unrelated_query_does_not_claim_a_match(self):
        found = Catalog(load_index).discover([ROOT / "references/index.json"], "zzunrelated731zz")
        self.assertTrue(found["complete"])
        self.assertEqual(found["references"], [])


if __name__ == "__main__":
    unittest.main()
