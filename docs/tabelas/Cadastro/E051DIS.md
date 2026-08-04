# E051DIS

## Descrição

Tabelas - Impostos - Dispositivos Fiscais

---

## Resumo

- Campos: 94
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDfs | Number(006,0) | Não | Código do dispositivo fiscal |
| DesDfs | String(150) | Não | Descrição do dispositivo fiscal |
| CodObs | String(020) | Sim | Código da Observação utilizada no SPED Fiscal e Sped Contribuições |
| AplDis | Number(002,0) | Sim | Aplicação do dispositivo fiscal |
| CodFif | String(015) | Sim | Código fiscal federal do dispositivo fiscal |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(015) | Sim | Código fiscal municipal do dispositivo fiscal |
| DocFis | String(001) | Sim | Permite associação do dispositivo fiscal ao documento fiscal |
| CodMsg | Number(004,0) | Sim | Código da mensagem da nota fiscal de saída |
| FunLeg | String(150) | Sim | Descrição referente a fundamentação legal |
| IniVid | Date | Sim | Data de início da vigência do dispositivo fiscal |
| FimVid | Date | Sim | Data final da vigência do dispositivo fiscal |
| SigUfs | String(002) | Sim | Sigla do estado referente tabela 5.3 do EFD |
| Gec197 | String(001) | Não | Indicação se deve gerar o registro C197/C597 do SPED Fiscal |
| Ged197 | String(001) | Não | Indicação se deve gerar o registro D197 do SPED Fiscal |
| RefIcm | Number(001,0) | Sim | Reflexo na apuração do ICMS referente tabela 5.3 do EFD |
| TipApu | Number(001,0) | Sim | Tipo de apuração de ICMS referente tabela 5.3 do EFD |
| ResIcm | Number(001,0) | Sim | Responsabilidade da apuração referente tabela 5.3 do EFD |
| InfRec | Number(001,0) | Sim | Influência no recolhimento do ICMS referente tabela 5.3 do EFD |
| OriTri | Number(001,0) | Sim | Origem da tributação referente tabela 5.3 do EFD |
| AjuIcm | Number(003,0) | Sim | Ajuste de ICMS referente tabela 5.3 do EFD |
| NumDae | String(020) | Sim | Número do documento de arrecadação estadual |
| NumPrs | String(255) | Sim | Número do processo de ajuste da apuração |
| OriPrs | Number(001,0) | Sim | Indicador da origem do processo de ajuste da apuração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Código do usuário responsável pela última atualização do registro |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |
| CodAjs | String(020) | Sim | Código do ajuste da apuração e dedução referente tabela 5.1.1 do EFD |
| CodInf | String(020) | Sim | Código da informação adicional referente tabela 5.2 do EFD |
| CodObr | String(003) | Sim | Código da obrigação a recolher conforme tabela 5.4 do EFD |
| CodAip | String(020) | Sim | Código do ajuste da apuração de IPI referente tabela 4.5.4 do EFD |
| EquLeg | Number(004,0) | Sim | Código do enquadramento legal |
| CodGer | Number(002,0) | Sim | Código da hipótese de geração de crédito acumulado de ICMS conforme inciso do arquivo 71 do RICMS/SP |
| AneIcm | String(010) | Sim | Anexo do RICMS/SP referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado do ICMS |
| ArtIcm | String(010) | Sim | Artigo referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado |
| IncIcm | String(010) | Sim | Inciso referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado |
| AliIcm | String(010) | Sim | Alínea referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado |
| PrgIcm | String(010) | Sim | Parágrafo referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado |
| ItmIcm | String(010) | Sim | Item do RICMS/SP referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado do ICMS |
| LtrIcm | String(010) | Sim | Letra do RICMS/SP referente ao enquadramento legal da operação ou prestação geradora de crédito acumulado do ICMS |
| CodImp | String(003) | Sim | Código do Imposto |
| AjsSpc | Number(002,0) | Sim | Código do ajuste do crédito ou contribuição do SPED Pis/Cofins (4.3.8) |
| IdeSec | String(030) | Sim | Identificação da seção judiciária onde foi ajuizado processo judicial |
| IdeVar | String(004) | Sim | Identificação da vara da seção judiciária onde foi ajuizado o processo judicial |
| NatAca | Number(002,0) | Sim | Identificação da natureza da ação judicial ou processo administrativo |
| DesDei | String(100) | Sim | Descrição resumida dos efeitos tributários abrangidos pela decisão judicial |
| DatDei | Date | Sim | Data da decisão judicial ou administrativa |
| VenAjs | String(001) | Sim | Indicativo se o valor do ajuste considera no total da nota fiscal saída |
| TpoCre | String(004) | Sim | Tipo de Utilização do Crédito tabela 5.5 do EFD |
| TipAjs | String(001) | Sim | Tipo de Ajuste do Documento Fiscal |
| MotEst | Number(001,0) | Sim | Motivo Estorno Crédito (DAPI-MG) |
| PerAjs | Number(007,4) | Sim | Percentual do Ajuste |
| TipAto | Number(002,0) | Sim | Tipo do Ato Legal |
| NumAto | String(060) | Sim | Número do Ato Legal |
| AnoAto | Number(004,0) | Sim | Ano do Ato Legal |
| EspBen | Number(002,0) | Sim | Espécie do Benefício Fiscal |
| RegGia | Number(001,0) | Sim | Anexo GIA RS |
| Re1400 | String(001) | Não | Indicação se deve gerar o registro 1400 do SPED Fiscal |
| IndMat | Number(002,0) | Sim | Indicativo da Matéria do Processo |
| IndAut | Number(002,0) | Sim | Indicativo da autoria da ação judicial |
| CepVar | Number(008,0) | Sim | CEP Seção Judiciária |
| Rec197 | Number(001,0) | Sim | Local onde o valor do ajuste será lançado no documento fiscal (Imposto / Outros) |
| Ree113 | String(001) | Sim | Gerar detalhamento por documento fiscal no registro E113 do SPED Fiscal |
| IndDde | Number(001,0) | Sim | Indicativo se o débito especial deve ser apresentado considerando a data de emissão ou data de entrada da nota fiscal. |
| CptGer | Date | Sim | Competência da geração EFD-Reinf |
| AltCmp | String(001) | Sim | Alteração do processo EFD-Reinf |
| CodAut | String(012) | Sim | Código de autorização para apropriação do crédito acumulado para a GIA - SP |
| InfBnf | String(001) | Sim | Utilizar a informação adicional como benefício fiscal |
| CodIna | String(008) | Sim | Código da informação adicional para o registro C177 do SPED Fiscal |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| AjsBas | String(020) | Sim | Código de Ajuste Base de Cálculo PIS/Cofins |
| CodCst | String(002) | Sim | Código da situação tributária do PIS ou do COFINS |
| DocMan | String(001) | Sim | Listar documentos fiscais do mês anterior no registro E113 do Sped Fiscal |
| NovIni | Date | Sim | Nova validade Inicial Reinf |
| NovFim | Date | Sim | Nova validade Final Reinf |
| Rd1400 | String(001) | Sim | Define se o registro 1400 será exportador pelo remetente ou destinatário |
| MotEsd | Number(001,0) | Sim | Motivo Estorno Débito (DAPI-MG) |
| LisPrd | String(001) | Sim | Listar produto nos registros C197, C597 e D197 do SPED ICMS/IPI |
| ConVlr | String(001) | Sim | Totalizar valor de outros ao valor de ajustes nos ajustes do item da nota fiscal |
| TipAtc | Number(002,0) | Sim | Tipo do ato concessório |
| AjsDpa | String(015) | Sim | Detalhamento dos outros créditos/débitos da apuração do ICMS para DIEF-PA (registro 18 e 19) |
| GeE116 | String(001) | Sim | Ind. se o reg. E116 poderá ser gerado a partir dos reg. C197,C597,C857,C897 e D197 do SPED ICMS IPI |
| ParImd | String(001) | Sim | Considerar parcelamento ICMS Diferido operações internas no E111 do SPED ICMS/IPI. |
| TprDis | Number(001,0) | Sim | Indicativo de qual título vai gerar no fechamento da nota fiscal |
| CodTpt | String(003) | Sim | Código de Tipo de Título |
| CbfCre | String(010) | Sim | Código do Benefício Fiscal de crédito presumido aplicado ao item |
| PerCre | Number(007,4) | Sim | Percentual de crédito presumido |
| CbfRbc | String(010) | Sim | Código de Benefício Fiscal de redução de base de cálculo |
| BcaIvi | String(001) | Sim | Base de cálculo no ajuste será igual ao valor do imposto |
| PerOut | String(001) | Sim | Valor Outros do registro C197 do SPED Fiscal é um percentual |

---

## Chave Primária

- CodEmp
- CodDfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
