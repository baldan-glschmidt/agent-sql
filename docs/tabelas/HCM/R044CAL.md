# R044CAL

## Descrição

Códigos de Cálculo

---

## Resumo

- Campos: 79
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| SitCal | String(001) | Sim | Situação do Cálculo |
| PerRef | Date | Sim | Competência do Cálculo |
| DatPag | Date | Sim | Data do Pagamento |
| IniCmp | Date | Sim | Data Início Período Folha |
| FimCmp | Date | Sim | Data Final Período Folha |
| CodOri | Number(005,0) | Sim | Código Origem - F.Complementar |
| IniVtr | Date | Sim | Início competência vtr |
| FimVtr | Date | Sim | Fim competência vtr |
| IniFvt | Date | Sim | Início Competência Faltas Vtr |
| FimFvt | Date | Sim | Fim Competência Faltas Vtr |
| IniApu | Date | Sim | Data Início Período Apuração Ponto |
| FimApu | Date | Sim | Data Final Período Apuração Ponto |
| IniAce | Date | Sim | Data Início Período Acerto Ponto |
| FimAce | Date | Sim | Data Final Período Acerto Ponto |
| IapCom | Date | Sim | Data Início Apuração Comissões |
| FapCom | Date | Sim | Data Final Apuração Comissões |
| IniVal | Date | Sim | Início competência vales |
| FimVal | Date | Sim | Fim competência vales |
| IniFvl | Date | Sim | Início Competência Faltas Vales |
| FimFvl | Date | Sim | Fim Competência Faltas Vales |
| GruCal | Number(003,0) | Sim | Grupo de Empresas (inclui o cálculo automaticamente p/ todas) |
| TipCao | Number(002,0) | Sim | Tipo do Cálculo de Origem na Folha Complementar |
| CalDes | String(001) | Sim | Outros Descontos em Folha Complementar |
| ConEst | String(001) | Sim | Considerar Estouro na Folha Complementar |
| DifFol | String(001) | Sim | Gerar Diferença na Próxima Folha |
| MsgEnv | String(070) | Sim | Mensagem do Envelope |
| MsgAni | String(070) | Sim | Mensagem do Envelope Se Colaborador Estiver de Aniversário |
| FolSim | String(001) | Sim | Folha Simulada |
| QtdDia | Number(002,0) | Sim | Quantidade de dias na segunda quinzena |
| QtdUte | Number(002,0) | Sim | Quantidade de dias úteis no cálculo |
| QtdDsr | Number(002,0) | Sim | Quantidade de DSRs no cálculo |
| PosAno | Number(002,0) | Sim | Ordem do Cálculo dentro do Ano |
| TipPar | Number(001,0) | Sim | Parcelado |
| CodPar | Number(005,0) | Sim | Código de Cálculo da 1ª Parcela Dissídio |
| CodPro | Number(011,0) | Sim | Código do Processo |
| AnoPro | Number(004,0) | Sim | Ano do Processo |
| NumJcj | Number(005,0) | Sim | Número da Vara/JCJ |
| IniPro | Date | Sim | Início do Processo |
| FimPro | Date | Sim | Fim do Processo |
| DatLei | Date | Sim | Data da Lei que determinou o reajuste retroativo |
| NumLei | String(012) | Sim | Número da Lei que determinou o reajuste retroativo |
| EftLei | Date | Sim | Data de Início do Efeito da Lei que determinou o reajuste retroativo |
| QtdPar | Number(002,0) | Sim | Quantidade de Parcelas |
| PerPar | Number(004,2) | Sim | Percentual da Parcela |
| Per13s | Number(005,2) | Sim | Percentual de adiantamento de 13° salário |
| ProImp | String(001) | Sim | Provisionar INSS/IRRF no adiantamento de 13° salário |
| Med13s | Number(001,0) | Sim | Pagar médias no adiatamento de  13° salário |
| AtvAce | String(001) | Sim | Liberar Acertos no Portal Web |
| AtvFol | String(001) | Sim | Liberar Folha no Portal Web |
| CmpDis | Date | Sim | Competência do Dissídio |
| DatEft | Date | Sim | Data Início do Efeito do Dissídio |
| ObsDis | String(255) | Sim | Observação do Dissídio |
| CmpHdi | String(001) | Sim | Considera Histórico GPS/Sefip |
| ObsCal | String(030) | Sim | Observação do Cálculo |
| CodLot | Number(004,0) | Sim | Código do Lote |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrSin | String(100) | Sim | Abrangência de Sindicato |
| CalAdi | Number(001,0) | Sim | Calcular |
| DatDis | Date | Sim | Data Homologação do Dissídio |
| EnvEso | Number(001,0) | Sim | Envio S-1200 eSocial |
| TipAco | Number(001,0) | Sim | Tipo de Acordo |
| RecTra | Number(001,0) | Sim | Reclamatória Trabalhista eSocial |
| En1202 | String(001) | Sim | Envio Periódicos eSocial |
| IniVlt | Date | Sim | Início Competência Vales Intermitente |
| FimVlt | Date | Sim | Fim Competência Vales Intermitente |
| IniFlt | Date | Sim | Início Competência Vales Faltas Intermitente |
| FimFlt | Date | Sim | Fim Competência Vales Faltas Intermitente |
| DisRcs | Number(001,0) | Sim | Pagamento de Rescisão Complementar do Dissídio |
| TipPro | Number(001,0) | Sim | Tipo do Processo referente ao Rendimentos Recebidos Acumuladamente - RRA |
| NumPro | String(021) | Sim | Número do Processo referente ao Rendimentos Recebidos Acumuladamente - RRA |
| NatPro | String(050) | Sim | Natureza do Rendimento Recebidos Acumuladamente - RRA |
| PagPlr | Number(001,0) | Sim | Informar se houve pagamento de PLR na rescisão |
| CplPlr | Number(005,0) | Sim | Informar qual o cálculo da rescisão complementar que houve o pagamento |
| EnvPlr | String(001) | Sim | Envio Periódicos eSocial Rescisão Complementar PLR |
| USU_DatPagRea | Date | Sim | Data de Pagamento Real |

---

## Chave Primária

- NumEmp
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044CAL_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

