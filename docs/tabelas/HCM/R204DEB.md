# R204DEB

## Descrição

Débitos do Período de Licença Especial

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| SeqPer | Number(003,0) | Não | Sequência Período |
| SeqDeb | Number(002,0) | Não | Sequência do Débito |
| IniGoz | Date | Sim | Data de Início do Gozo da Licença Especial |
| FimGoz | Date | Sim | Fim do Gozo da Licença Especial |
| DatPag | Date | Sim | Data de Pagamento (se não foi gozado) |
| QtdDli | Number(004,0) | Sim | Quantidade de Dias de Licença (gozados ou pagos) |
| TipDeb | String(001) | Sim | Tipo de Débito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqPer
- SeqDeb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R204DEB_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R204DEB_003

**Tabela:** R204PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqPer | SeqPer |

