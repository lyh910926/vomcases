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
    default:
      class: Directory
      listing: []
      path: ../../work/HowardSprings/freedrainage_cpcff2.2/params_nf2.2/input
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_4:
    default: data/VOM_output/HowardSprings/freedrainage_cpcff2.2/params_nf
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../work/HowardSprings/freedrainage_cpcff2.2/params_nf2.2/vom_namelist
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
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
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff2.2/params_nf
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_sh/run_vom.sh
    writable: false
  - entry: $(inputs.input_2)
    entryname: src/VOM/VOM_Fortran
    writable: false
  - entry: $(inputs.input_3)
    entryname: work/HowardSprings/freedrainage_cpcff2.2/params_nf2.2/input
    writable: false
  - entry: $(inputs.input_5)
    entryname: work/HowardSprings/freedrainage_cpcff2.2/params_nf2.2/vom_namelist
    writable: false
successCodes: []
temporaryFailCodes: []
