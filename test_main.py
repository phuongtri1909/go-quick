from main import CCCDExtractor
import json

#CCCD EXTRACTOR 
# go_quick = CCCDExtractor()
# task = {
#     "func_type": 1,
#     "inp_path": "./datatest",
# }
# results = go_quick.handle_task(task)
# print(json.dumps(results,ensure_ascii=False,indent=2))

#PDF2PNG 
# go_quick = CCCDExtractor()
# task = {
#     "func_type": 2,
#     "inp_path": "./datatest",
# }
# results = go_quick.handle_task(task)
# if results["status"] == "success":
#     import base64
#     zip_bytes = base64.b64decode(results["zip_base64"])
#     with open("test_download.zip", "wb") as f:
#         f.write(zip_bytes)
# print(json.dumps(results,ensure_ascii=False,indent=2))

#XLSX2PNG 
# go_quick = CCCDExtractor()
# task = {
#     "func_type": 3,
#     "inp_path": r"C:\Users\PC\Desktop\tách source\ID Quick 2025\datatest\cccd_excel.xlsx",
# }
# results = go_quick.handle_task(task)
# if results["status"] == "success":
#     import base64
#     zip_bytes = base64.b64decode(results["zip_base64"])
#     with open("test_download.zip", "wb") as f:
#         f.write(zip_bytes)
# print(json.dumps(results,ensure_ascii=False,indent=2))
