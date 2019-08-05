arguments: []
baseCommand:
- wc
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_stdin:
    default:
      class: File
      path: ../../data/Silo/adelaide.txt
    streamable: false
    type: File
outputs:
  output_stdout:
    streamable: false
    type: stdout
permanentFailCodes: []
requirements: []
stdin: $(inputs.input_stdin.path)
stdout: wc_adelaide
successCodes: []
temporaryFailCodes: []
