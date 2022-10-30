#엑셀파일 생성 코드
import pandas as pd
df = pd.DataFrame(
    [["홍길동",	"1990.01.02",	"2021-0001"],
        ["김민준",	"1990.01.02",	"2021-0002"],
        ["김철수",	"1990.01.02",	"2021-0003"],
        ["김영희",	"1990.01.02",	"2021-0004"],
        ["이서준",	"1990.01.02",	"2021-0005"],
        ["장다인",	"1990.01.02",	"2021-0006"]])

print(df)
df.to_excel(r'/workspaces/python_40projects/automation_programs/엑셀의 정보를 불러와 수료증 자동 생성/수료증명단.xlsx', index = False, header=False)