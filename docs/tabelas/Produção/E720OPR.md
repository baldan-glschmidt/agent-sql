# E720OPR

## Descrição

Ficha - Roteiro - Cadastro de Operações de Fabricação

---

## Resumo

- Campos: 29
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOpr | String(006) | Não | Código da operação |
| DesOpr | String(040) | Não | Descrição da operação |
| AbrOpr | String(010) | Não | Abreviatura da operação |
| CodCre | String(008) | Não | Código do centro de recursos |
| UtiOpr | String(001) | Não | Indicativo se a operação oferece dados automaticamente para o roteiro |
| TmpPrp | Number(010,4) | Sim | Tempo proporcional de execuação da operação |
| TmpFix | Number(010,4) | Sim | Tempo de fixo de execuação da operação, em função do lote técnico |
| TmpFrq | Number(012,3) | Sim | Tempo frequencial de execuação da operação, em função da quantidade frequencial |
| QtdFrq | Number(014,5) | Sim | Quantidade utilizada para dimensionar o tempo frequencial |
| UniCre | String(001) | Não | Unidade de medida dos tempos (S=Segundo; M=Minuto; H=Hora; D=Dia) |
| CodEtg | Number(004,0) | Sim | Código do estágio em que a operação será utilizada |
| ObsOpr | String(240) | Sim | Observações sobre a operação |
| DatAlt | Date | Sim | Data da geração ou alteração dos tempos da operação |
| UsoCus | String(001) | Sim | Indicativo se é utilizado para formação preço de custos |
| CodCcu | String(009) | Sim | Código do centro de custos |
| CodUsu | Number(010,0) | Sim | Usuário de alteração do registro |
| PerEfi | Number(005,2) | Sim | Percentual de eficiência de produção da operação |
| CapSmt | Number(014,5) | Sim | Capacidade produtiva simultânea (por unidade de produto) |
| MovAut | String(001) | Sim | Indicativo se a operação inicia automaticamente após o fim da anterior |
| LotTec | Number(010,3) | Sim | Lote técnico ideal de fabricação, a nível de operação |
| DtiVal | Date | Sim | Data de validade inicial para utilização desta operação |
| DtfVal | Date | Sim | Data de validade final para utilização desta operação |
| SelCus | String(001) | Não | Indicativo se será considerado para área de custos (importação de ficha técnica) |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| VerOpr | String(015) | Sim | Última versão da operação (é incrementada em cada nova alteração) |
| MovOrp | String(001) | Sim | Indicativo se gera movimentação em OP |
| IndIcp | String(001) | Sim | Indicativo se a operação permite a incorporação de produtos na OP |
| IndSer | String(001) | Sim | Indicativo de uso exlusivo para roteiro de OS |

---

## Chave Primária

- CodEmp
- CodOpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E720OPR_004

**Tabela:** E725CRE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCre | CodCre |

