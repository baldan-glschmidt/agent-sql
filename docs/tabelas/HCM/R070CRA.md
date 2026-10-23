# R070CRA

## Descrição

Créditos de Acesso por Aluno

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
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

- NumMat
- VerPlf
- CodPlf
- DatIni
- IniFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070CRA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

