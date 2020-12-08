arguments: []
baseCommand:
- cp
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/3_modeltime/dailyweather.prn
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default: work/additional_analyses/comp2015/3_modeltime/best/input/dailyweather.prn
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_2)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/comp2015/3_modeltime/best/input
    writable: true
  - entry: $(inputs.input_1)
    entryname: data/VOM_input/HowardSprings/3_modeltime/dailyweather.prn
    writable: false
successCodes: []
temporaryFailCodes: []
