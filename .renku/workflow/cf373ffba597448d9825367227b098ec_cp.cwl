arguments: []
baseCommand:
- cp
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: Directory
      listing: []
      path: ../../work/DalyUncleared/freedrainage_cpcff2.0/best
    inputBinding:
      position: 1
      prefix: -r
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_2:
    default: DalyUncleared/nofreedrainage_cpcff2.0/best_free/
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: work/DalyUncleared/nofreedrainage_cpcff2.0/best_free/vom_namelist
    streamable: false
    type: File
permanentFailCodes: []
requirements: []
successCodes: []
temporaryFailCodes: []
