arguments: []
baseCommand:
- jupyter
- nbconvert
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default: latex
    inputBinding:
      position: 1
      prefix: --to
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_2:
    default: hidecode.tpl
    inputBinding:
      position: 2
      prefix: --template
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_3:
    default:
      class: File
      path: ../../notebooks/additional_analyses/S1_comp2015.ipynb
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default: data/supplements/S1_comp2015
    inputBinding:
      position: 4
      prefix: --output-dir=
      separate: false
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_4)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/supplements/S1_comp2015
    writable: true
  - entry: $(inputs.input_3)
    entryname: notebooks/additional_analyses/S1_comp2015.ipynb
    writable: false
successCodes: []
temporaryFailCodes: []
