# R135PCO

## Descrição

Disponibilidade Horário - Pessoa p/Competência

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CmpDis | Date | Não | Competência p/Disponibilidade de Horário |
| ObsDis | String(200) | Sim | Observação |

---

## Chave Primária

- CodPes
- CmpDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R135PCO_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

