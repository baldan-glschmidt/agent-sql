# R070CRO

## Descrição

Créditos de Acesso por Colaborador de Outra Unidade

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador de Outra Unidade |
| DatIni | Date | Não | Data Inicial da Faixa de Crédito |
| DatFim | Date | Sim | Data Final da Faixa de Crédito |
| IniFai | Number(005,0) | Não | Hora de Início da Faixa de Crédito |
| FimFai | Number(005,0) | Sim | Hora Fim da Faixa de Crédito |
| CreDia | Number(002,0) | Sim | Qtde de Créditos por Dia Segundo a Faixa |
| StaAcc | Number(001,0) | Sim | Status do Crédito de Acesso |
| SalAnt | Number(003,0) | Sim | Saldo anterior do crédito de acesso |
| SalAtu | Number(003,0) | Sim | Saldo atual do crédito de acesso |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |
| LimCon | Number(002,0) | Sim | Limite de consumo diário na faixa |
| QtdCon | Number(003,0) | Sim | Quantidade consumida na faixa no dia |
| DatCon | Date | Sim | Data do último consumo na faixa |
| HorCon | Number(005,0) | Sim | Hora do Consumo |

---

## Chave Primária

- NumEmp
- NumCad
- VerPlf
- CodPlf
- DatIni
- IniFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070CRO_001

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

