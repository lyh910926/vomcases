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
      path: ../../work/additional_analyses/sens_delz/HS_1.00/best0.50/input
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_4:
    default: data/VOM_output/additional_analyses/sens_delz/HS_1.00/sce_best0.50
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_5:
    default:
      class: File
      path: ../../work/additional_analyses/sens_delz/HS_1.00/best0.50/vom_namelist
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
    entryname: data/VOM_output/additional_analyses/sens_delz/HS_1.00/sce_best0.50
    writable: true
successCodes: []
temporaryFailCodes: []
