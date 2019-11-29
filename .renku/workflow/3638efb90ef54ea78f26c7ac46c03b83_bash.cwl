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
      path: ../../work/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/input
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_4:
    default:
      class: File
      path: ../../data/VOM_input/AdelaideRiver/dailyweather.prn
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../data/VOM_soils/AdelaideRiver/deepsoils/soilprofile.par
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../work/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/vom_namelist
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default: data/VOM_output/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/sce2
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_8:
    default:
      class: Directory
      listing: []
      path: ../../data/VOM_output/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/sce
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
outputs:
  output_0:
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
  - entry: $(inputs.input_3)
    entryname: work/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/input
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_input/AdelaideRiver/dailyweather.prn
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_soils/AdelaideRiver/deepsoils/soilprofile.par
    writable: false
  - entry: $(inputs.input_6)
    entryname: work/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/vom_namelist
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/VOM_output/additional_analyses/deep_soils/AdelaideRiver/freedrainage_cpcff0.2/sce
    writable: false
successCodes: []
temporaryFailCodes: []
