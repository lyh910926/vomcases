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
  input_10:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/watbal.f90
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: Directory
      listing: []
      path: ../../work/DryRiver/nofreedrainage_cpcff1.4
    inputBinding:
      position: 2
      separate: true
      shellQuote: true
    streamable: false
    type: Directory
  input_3:
    default:
      class: File
      path: ../../data/VOM_input/DryRiver/dailyweather.prn
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default:
      class: File
      path: ../../work/DryRiver/nofreedrainage_cpcff1.4/vom_namelist
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_5:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/coreprog.f90
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/modules.f90
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_7:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sample.f90
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/sce.f90
    inputBinding:
      position: 8
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../src/VOM/VOM_Fortran/VOM-code/transpmodel.f90
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_bestpars.txt
    streamable: false
    type: File
  output_1:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_progress.txt
    streamable: false
    type: File
  output_2:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_lastbest.txt
    streamable: false
    type: File
  output_3:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_out.txt
    streamable: false
    type: File
  output_4:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_status.txt
    streamable: false
    type: File
  output_5:
    outputBinding:
      glob: data/VOM_output/DryRiver/nofreedrainage_cpcff1.4sce_lastloop.txt
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/VOM_output/DryRiver
    writable: true
successCodes: []
temporaryFailCodes: []
