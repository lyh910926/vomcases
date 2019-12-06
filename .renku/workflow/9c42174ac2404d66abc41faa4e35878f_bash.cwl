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
      path: ../../src_sh/run_vom.sh
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
    default: work/DryRiver/freedrainage_cpcff2.4/input
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_4:
    default:
      class: File
      path: ../../data/VOM_input/DryRiver/dailyweather.prn
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/VOM_soils/DryRiver/soilprofile.par
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../work/DryRiver/freedrainage_cpcff2.4/vom_namelist
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: data/VOM_output/DryRiver/freedrainage_cpcff2.4/sce
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_3)
    streamable: false
    type: Directory
  output_1:
    outputBinding:
      glob: $(inputs.input_7)
    streamable: false
    type: Directory
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: $(inputs.input_1)
    entryname: src_sh/run_vom.sh
    writable: false
  - entry: $(inputs.input_2)
    entryname: src/VOM/VOM_Fortran
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_input/DryRiver/dailyweather.prn
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_soils/DryRiver/soilprofile.par
    writable: false
  - entry: $(inputs.input_6)
    entryname: work/DryRiver/freedrainage_cpcff2.4/vom_namelist
    writable: false
successCodes: []
temporaryFailCodes: []
