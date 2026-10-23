# R026FPV

## Descrição

Códigos do FPAS - Valores

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFpa | Number(003,0) | Não | Código do FPAS |
| TipGrp | Number(001,0) | Não | Tipo da GPS |
| DatFpa | Date | Não | Data de Início da Vigência |
| PerEmp | Number(005,2) | Sim | Percentual da Empresa |
| PerTer | Number(007,4) | Sim | Percentual de Terceiros do FPAS |
| CodTer | Number(004,0) | Sim | Código de Terceiros |
| PerDir | Number(005,2) | Sim | Percentual dos Diretores |
| PerAut | Number(005,2) | Sim | Percentual de Autônomos |
| PerCoo | Number(005,2) | Sim | Percentual de Cooperativas de Trabalho |
| PerEmF | Number(005,2) | Sim | % Empresa Física/Adquirente |
| PerEmJ | Number(005,2) | Sim | % Empresa Jurídica |
| PerPEm | Number(005,2) | Sim | % Empresa Patrocínio/Ev. Desportivos |
| PerRat | Number(005,2) | Sim | Percentual RAT |
| CodTCo | Number(004,0) | Sim | Código de Terceiros p/ Cooperativas |
| PerTCo | Number(007,4) | Sim | Percentual de Terceiros p/ Cooperativas |
| PerRaJ | Number(005,2) | Sim | Percentual RAT Jurídica |

---

## Chave Primária

- CodFpa
- TipGrp
- DatFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026FPV_000

**Tabela:** R026FPA

| Origem | Destino |
|--------|---------|
| CodFpa | CodFpa |

