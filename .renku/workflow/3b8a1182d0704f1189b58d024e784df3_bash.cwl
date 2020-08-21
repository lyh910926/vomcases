arguments: []
baseCommand:
- bash
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_sh/run_vom2015.sh
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: Directory
      listing: []
      path: ../../src/VOM/VOM_Fortran
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_3:
    default:
      class: Directory
      listing: []
      path: ../../data/VOM_input/HowardSprings/9_weather
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_4:
    default:
      class: File
      path: ../../data/VOM_input/HowardSprings/9_weather/dailyweather.prn
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../work/additional_analyses/comp2015/9_weather/vom_namelist
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default: data/VOM_output/additional_analyses/comp2015/9_weather/sce
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_6)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: $(inputs.input_1)
    entryname: src_sh/run_vom2015.sh
    writable: false
  - entry: $(inputs.input_2)
    entryname: src/VOM/VOM_Fortran
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_input/HowardSprings/9_weather
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_input/HowardSprings/9_weather/dailyweather.prn
    writable: false
  - entry: $(inputs.input_5)
    entryname: work/additional_analyses/comp2015/9_weather/vom_namelist
    writable: false
successCodes: []
temporaryFailCodes: []
