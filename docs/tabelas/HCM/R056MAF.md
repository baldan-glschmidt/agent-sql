# R056MAF

## Descrição

Mestre Atraso FGTS

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpMaf | Date | Não | Competência do Atraso |
| DatVen | Date | Sim | Data do Vencimento |
| UltPag | String(001) | Sim | Assinalamento do Ultimo Pagto |
| USU_TIPREC | Number(001,0) | Sim | Tipo Recolhimento |

---

## Chave Primária

- NumEmp
- CmpMaf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056MAF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

