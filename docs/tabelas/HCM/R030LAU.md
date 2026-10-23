# R030LAU

## Descrição

Filiais da Empresa - Histórico Responsável LTCAT

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatIni | Date | Não | Data em que assumiu a responsabilidade |
| EmpLau | Number(004,0) | Não | Código da empresa do responsável pelo LTCAT |
| TipCol | Number(001,0) | Não | Tipo do Responsável pelo LTCAT |
| NumCad | Number(009,0) | Não | Cadastro do Responsável pelo LTCAT |
| DatTer | Date | Sim | Data em que encerrou a responsabilidade |
| AssDig | Image | Sim | Assinatura Digitalizada |

---

## Chave Primária

- NumEmp
- CodFil
- DatIni
- EmpLau
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030LAU_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

