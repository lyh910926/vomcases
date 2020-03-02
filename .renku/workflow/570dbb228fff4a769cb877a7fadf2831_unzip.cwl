arguments: []
baseCommand:
- unzip
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../data/data_from_a_model_inter/SavMIP.zip
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: data/SavMIP_extracted
    inputBinding:
      position: 2
      prefix: -d
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_2)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/SavMIP_extracted
    writable: true
  - entry: $(inputs.input_1)
    entryname: data/data_from_a_model_inter/SavMIP.zip
    writable: false
successCodes: []
temporaryFailCodes: []
