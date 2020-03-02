arguments: []
baseCommand:
- python3
class: CommandLineTool
cwlVersion: v1.0
hints: []
inputs:
  input_1:
    default:
      class: File
      path: ../../src_py/plot_ensembleyears.py
    inputBinding:
      position: 1
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_10:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    inputBinding:
      position: 10
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_11:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/DryRiver.csv
    inputBinding:
      position: 11
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_12:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/SturtPlains.csv
    inputBinding:
      position: 12
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_13:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/HowardSprings_ET_GPP.csv
    inputBinding:
      position: 13
      prefix: --bios2
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_14:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/AdelaideRiver_ET_GPP.csv
    inputBinding:
      position: 14
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_15:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    inputBinding:
      position: 15
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_16:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/DryRiver_ET_GPP.csv
    inputBinding:
      position: 16
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_17:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BIOS2/SturtPlains_ET_GPP.csv
    inputBinding:
      position: 17
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_18:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/howard_springs/howard_springs_et_eco.txt
    inputBinding:
      position: 18
      prefix: --lpjguess
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_19:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/adelaide_river/adelaide_river_et_eco.txt
    inputBinding:
      position: 19
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_2:
    default:
      class: File
      path: ../../data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 2
      prefix: --vom
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_20:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    inputBinding:
      position: 20
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_21:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/dry_river/dry_river_et_eco.txt
    inputBinding:
      position: 21
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_22:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/sturt_plains/sturt_plains_et_eco.txt
    inputBinding:
      position: 22
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_23:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/howard_springs/howard_springs_gpp_eco.txt
    inputBinding:
      position: 23
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_24:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/adelaide_river/adelaide_river_gpp_eco.txt
    inputBinding:
      position: 24
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_25:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    inputBinding:
      position: 25
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_26:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/dry_river/dry_river_gpp_eco.txt
    inputBinding:
      position: 26
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_27:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/LPJGUESS/sturt_plains/sturt_plains_gpp_eco.txt
    inputBinding:
      position: 27
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_28:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/HowardSprings_savannas_maespa_simulation.csv
    inputBinding:
      position: 28
      prefix: --maespa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_29:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/AdelaideRiver_savannas_maespa_simulation.csv
    inputBinding:
      position: 29
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_3:
    default:
      class: File
      path: ../../data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 3
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_30:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    inputBinding:
      position: 30
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_31:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/DryRiver_savannas_maespa_simulation.csv
    inputBinding:
      position: 31
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_32:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/MAESPA/SturtPlains_savannas_maespa_simulation.csv
    inputBinding:
      position: 32
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_33:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/howardsprings_hourly_outputs.csv
    inputBinding:
      position: 33
      prefix: --spa
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_34:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/adelaideriver_hourly_outputs.csv
    inputBinding:
      position: 34
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_35:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    inputBinding:
      position: 35
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_36:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/dryriver_hourly_outputs.csv
    inputBinding:
      position: 36
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_37:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/SPAv1/sturtplains_hourly_outputs.csv
    inputBinding:
      position: 37
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_38:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/HowardSprings_CABLE.nc
    inputBinding:
      position: 38
      prefix: --cable
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_39:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/AdelaideRiver_CABLE.nc
    inputBinding:
      position: 39
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_4:
    default:
      class: File
      path: ../../data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 4
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_40:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    inputBinding:
      position: 40
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_41:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/DryRiver_CABLE.nc
    inputBinding:
      position: 41
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_42:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/CABLE/SturtPlains_CABLE.nc
    inputBinding:
      position: 42
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_43:
    default: Howard Springs
    inputBinding:
      position: 43
      prefix: --sites
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_44:
    default: Litchfield
    inputBinding:
      position: 44
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_45:
    default: Adelaide River
    inputBinding:
      position: 45
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_46:
    default: Daly Uncleared
    inputBinding:
      position: 46
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_47:
    default: Dry River
    inputBinding:
      position: 47
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_48:
    default: Sturt Plains
    inputBinding:
      position: 48
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_49:
    default: 1
    inputBinding:
      position: 49
      prefix: --whitley_sites
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_5:
    default:
      class: File
      path: ../../data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 5
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_50:
    default: 0
    inputBinding:
      position: 50
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_51:
    default: 1
    inputBinding:
      position: 51
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_52:
    default: 1
    inputBinding:
      position: 52
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_53:
    default: 1
    inputBinding:
      position: 53
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_54:
    default: 1
    inputBinding:
      position: 54
      separate: true
      shellQuote: true
    streamable: false
    type: int
  input_55:
    default:
      class: File
      path: ../../data/DINGO/Ea_howard.txt
    inputBinding:
      position: 55
      prefix: --dingo_et
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_56:
    default:
      class: File
      path: ../../data/DINGO/Ea_litch.txt
    inputBinding:
      position: 56
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_57:
    default:
      class: File
      path: ../../data/DINGO/Ea_adelaide.txt
    inputBinding:
      position: 57
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_58:
    default:
      class: File
      path: ../../data/DINGO/Ea_daly.txt
    inputBinding:
      position: 58
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_59:
    default:
      class: File
      path: ../../data/DINGO/Ea_dry.txt
    inputBinding:
      position: 59
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_6:
    default:
      class: File
      path: ../../data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 6
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_60:
    default:
      class: File
      path: ../../data/DINGO/Ea_sturt.txt
    inputBinding:
      position: 60
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_61:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_howard.txt
    inputBinding:
      position: 61
      prefix: --dingo_gpp
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_62:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_litch.txt
    inputBinding:
      position: 62
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_63:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_adelaide.txt
    inputBinding:
      position: 63
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_64:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_daly.txt
    inputBinding:
      position: 64
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_65:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_dry.txt
    inputBinding:
      position: 65
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_66:
    default:
      class: File
      path: ../../data/DINGO/GPPdaily_sturt.txt
    inputBinding:
      position: 66
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_67:
    default:
      class: File
      path: ../../data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    inputBinding:
      position: 67
      prefix: --i2015
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_68:
    default: data/img/3_model_comparison.png
    inputBinding:
      position: 68
      prefix: -o
      separate: true
      shellQuote: true
    streamable: false
    type: string
  input_7:
    default:
      class: File
      path: ../../data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    inputBinding:
      position: 7
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_8:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/HowardSprings.csv
    inputBinding:
      position: 8
      prefix: --bess
      separate: true
      shellQuote: true
    streamable: false
    type: File
  input_9:
    default:
      class: File
      path: ../../data/SavMIP_extracted/SavMIP/BESS/AdelaideRiver.csv
    inputBinding:
      position: 9
      separate: true
      shellQuote: true
    streamable: false
    type: File
outputs:
  output_0:
    outputBinding:
      glob: $(inputs.input_68)
    streamable: false
    type: File
permanentFailCodes: []
requirements:
- class: InlineJavascriptRequirement
- class: InitialWorkDirRequirement
  listing:
  - entry: '$({"listing": [], "class": "Directory"})'
    entryname: data/img
    writable: true
  - entry: $(inputs.input_1)
    entryname: src_py/plot_ensembleyears.py
    writable: false
  - entry: $(inputs.input_2)
    entryname: data/VOM_output/HowardSprings/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_3)
    entryname: data/VOM_output/Litchfield/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_4)
    entryname: data/VOM_output/AdelaideRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_5)
    entryname: data/VOM_output/DalyUncleared/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_6)
    entryname: data/VOM_output/DryRiver/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_7)
    entryname: data/VOM_output/SturtPlains/freedrainage_cpcff1.0/sce_best/results_daily.txt
    writable: false
  - entry: $(inputs.input_8)
    entryname: data/SavMIP_extracted/SavMIP/BESS/HowardSprings.csv
    writable: false
  - entry: $(inputs.input_9)
    entryname: data/SavMIP_extracted/SavMIP/BESS/AdelaideRiver.csv
    writable: false
  - entry: $(inputs.input_10)
    entryname: data/SavMIP_extracted/SavMIP/BESS/DalyRiverUncleared.csv
    writable: false
  - entry: $(inputs.input_11)
    entryname: data/SavMIP_extracted/SavMIP/BESS/DryRiver.csv
    writable: false
  - entry: $(inputs.input_12)
    entryname: data/SavMIP_extracted/SavMIP/BESS/SturtPlains.csv
    writable: false
  - entry: $(inputs.input_13)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/HowardSprings_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_14)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/AdelaideRiver_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_15)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/DalyRiverUncleared_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_16)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/DryRiver_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_17)
    entryname: data/SavMIP_extracted/SavMIP/BIOS2/SturtPlains_ET_GPP.csv
    writable: false
  - entry: $(inputs.input_18)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/howard_springs/howard_springs_et_eco.txt
    writable: false
  - entry: $(inputs.input_19)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/adelaide_river/adelaide_river_et_eco.txt
    writable: false
  - entry: $(inputs.input_20)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_et_eco.txt
    writable: false
  - entry: $(inputs.input_21)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/dry_river/dry_river_et_eco.txt
    writable: false
  - entry: $(inputs.input_22)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/sturt_plains/sturt_plains_et_eco.txt
    writable: false
  - entry: $(inputs.input_23)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/howard_springs/howard_springs_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_24)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/adelaide_river/adelaide_river_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_25)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/daly_river_uncleared/daly_river_uncleared_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_26)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/dry_river/dry_river_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_27)
    entryname: data/SavMIP_extracted/SavMIP/LPJGUESS/sturt_plains/sturt_plains_gpp_eco.txt
    writable: false
  - entry: $(inputs.input_28)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/HowardSprings_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_29)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/AdelaideRiver_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_30)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/DalyRiverUncleared_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_31)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/DryRiver_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_32)
    entryname: data/SavMIP_extracted/SavMIP/MAESPA/SturtPlains_savannas_maespa_simulation.csv
    writable: false
  - entry: $(inputs.input_33)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/howardsprings_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_34)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/adelaideriver_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_35)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/dalyriveruncleared_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_36)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/dryriver_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_37)
    entryname: data/SavMIP_extracted/SavMIP/SPAv1/sturtplains_hourly_outputs.csv
    writable: false
  - entry: $(inputs.input_38)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/HowardSprings_CABLE.nc
    writable: false
  - entry: $(inputs.input_39)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/AdelaideRiver_CABLE.nc
    writable: false
  - entry: $(inputs.input_40)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/DalyRiverUncleared_CABLE.nc
    writable: false
  - entry: $(inputs.input_41)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/DryRiver_CABLE.nc
    writable: false
  - entry: $(inputs.input_42)
    entryname: data/SavMIP_extracted/SavMIP/CABLE/SturtPlains_CABLE.nc
    writable: false
  - entry: $(inputs.input_55)
    entryname: data/DINGO/Ea_howard.txt
    writable: false
  - entry: $(inputs.input_56)
    entryname: data/DINGO/Ea_litch.txt
    writable: false
  - entry: $(inputs.input_57)
    entryname: data/DINGO/Ea_adelaide.txt
    writable: false
  - entry: $(inputs.input_58)
    entryname: data/DINGO/Ea_daly.txt
    writable: false
  - entry: $(inputs.input_59)
    entryname: data/DINGO/Ea_dry.txt
    writable: false
  - entry: $(inputs.input_60)
    entryname: data/DINGO/Ea_sturt.txt
    writable: false
  - entry: $(inputs.input_61)
    entryname: data/DINGO/GPPdaily_howard.txt
    writable: false
  - entry: $(inputs.input_62)
    entryname: data/DINGO/GPPdaily_litch.txt
    writable: false
  - entry: $(inputs.input_63)
    entryname: data/DINGO/GPPdaily_adelaide.txt
    writable: false
  - entry: $(inputs.input_64)
    entryname: data/DINGO/GPPdaily_daly.txt
    writable: false
  - entry: $(inputs.input_65)
    entryname: data/DINGO/GPPdaily_dry.txt
    writable: false
  - entry: $(inputs.input_66)
    entryname: data/DINGO/GPPdaily_sturt.txt
    writable: false
  - entry: $(inputs.input_67)
    entryname: data/VOM_output/additional_analyses/comp2015/0_benchmark/resultsdaily.txt
    writable: false
successCodes: []
temporaryFailCodes: []
