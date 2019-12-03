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
    default: work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.2/input/
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
      path: ../../data/VOM_soils/DryRiver/deepsoils/soilprofile.par
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.2/vom_namelist
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.2/sce/
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
outputs:
  output_0:
    outputBinding:
      glob: work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/input/dailyweather.prn
    streamable: false
    type: File
  output_1:
    outputBinding:
      glob: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/sce/sce_out.txt
    streamable: false
    type: File
  output_2:
    outputBinding:
      glob: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/sce/sce_lastbest.txt
    streamable: false
    type: File
  output_3:
    outputBinding:
      glob: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/sce/sce_progress.txt
    streamable: false
    type: File
  output_4:
    outputBinding:
      glob: work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/input/soilprofile.par
    streamable: false
    type: File
  output_5:
    outputBinding:
      glob: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/sce/sce_bestpars.txt
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/input
    writable: true
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.4/sce
    writable: true
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
    entryname: data/VOM_soils/DryRiver/deepsoils/soilprofile.par
    writable: false
  - entry: $(inputs.input_6)
    entryname: work/additional_analyses/deep_soils/DryRiver/freedrainage_cpcff1.2/vom_namelist
    writable: false
successCodes: []
temporaryFailCodes: []
