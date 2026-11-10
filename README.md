# UX·UI·접근성 원천

이 원천은 디자인에서 판단할 영역·항목과 관련 근거의 참조를 관리합니다. 모델이 사용자 과제와 실제 근거를 바탕으로 적용 여부와 결과를 판단합니다. 제품 요구, 화면 템플릿, 합성 앱, 과제별 정답은 제공하지 않습니다.

`references/index.json`에서 영역별 하위 색인으로 들어갑니다. 주제별 상세는 해당 영역에 두며 원문 규약은 원래 출처를 참조합니다. 사용자 과제·결정·실행 결과는 소비자 프로젝트가 소유합니다.

`project-builder`에서 선택해 연결하는 독립 원천이며 내부 capability를 전역 설치하지 않습니다. `source.json`이 원천 정보, `source-files.json`이 공개 파일 목록입니다.

## 검증

선택한 참조 클라이언트의 경로로 실행합니다.

```sh
client_root=/path/to/project-builder
python3 "$client_root/scripts/validate_source.py" --source .
PYTHONPATH="$client_root/plugins/project-builder/scripts" python3 -m unittest discover -s tests -p 'test_*.py' -v
```

검사는 원천 계약과 질문에서 관련 근거까지의 발견 경로를 확인합니다. 모델의 판단 품질과 실제 제품의 동작·사용성은 별도 관찰 대상입니다.
