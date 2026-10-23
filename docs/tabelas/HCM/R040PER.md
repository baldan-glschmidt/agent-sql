# R040PER

## Descrição

Períodos de Férias

---

## Resumo

- Campos: 32
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IniPer | Date | Não | Data Início do Período |
| FimPer | Date | Sim | Data Fim do Período |
| QtdDir | Number(005,2) | Sim | Dias de Direito |
| QtdFal | Number(006,2) | Sim | Dias de Falta |
| QtdAfa | Number(007,2) | Sim | Dias de Afastamento |
| QtdLir | Number(006,2) | Sim | Dias de Licença Remunerada |
| QtdDeb | Number(005,2) | Sim | Dias de Débito |
| QtdLin | Number(007,2) | Sim | Dias de Licença Não Remunerada |
| QtdMil | Number(007,2) | Sim | Dias de Serviço Militar |
| QtdAbo | Number(005,2) | Sim | Dias de Abono Pecuniário |
| QtdSld | Number(005,2) | Sim | Dias de Saldo |
| QtdAbn | Number(005,2) | Sim | Dias Abonados (Dias de Férias Gozados s/ Saldo) |
| QtdAsd | Number(005,2) | Sim | Dias Assiduidade |
| QtdGas | Number(005,2) | Sim | Dias Gozados Assiduidade |
| AvoFer | Number(002,0) | Sim | Avos de Férias |
| AvoPer | Number(003,0) | Sim | Avos de Férias Perdidos |
| DiaCom | Number(002,0) | Sim | Dias a compensar |
| DiaDev | Number(002,0) | Sim | Dias Saldo Devedor |
| QtdPng | Number(005,2) | Sim | Dias Compensados (controle manual) |
| SitPer | Number(002,0) | Sim | Situação do Período |
| AltFim | String(001) | Sim | Alterou final do período |
| PerSus | String(001) | Sim | Período Suspenso |
| PagAdi | String(001) | Sim | Indica se já foi pago o adicional de férias deste período |
| QtdUte | Number(002,0) | Sim | Quantidade de dias úteis gozados nas férias |
| TotUte | Number(003,0) | Sim | Total Dias Úteis |
| TotU30 | Number(003,0) | Sim | Total Úteis 30 Dias |
| LimCon | Date | Sim | Data Limite Concessão de Férias |
| DiaInt | Number(005,2) | Sim | Dias Troca Categoria Intermitente |
| DatInt | Date | Sim | Data Fim Categoria Intermitente |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040PER_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

