# R026PLR

## Descrição

IRRF - PLR

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PerRef | Date | Não | Competência referênte ao IR |
| LimIse | Number(011,2) | Sim | Limite de Isenção |
| DesDep | Number(011,2) | Sim | Desconto por Dependente |
| VlrAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |

---

## Chave Primária

- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026PLR_000

**Tabela:** R026IRR

| Origem | Destino |
|--------|---------|
| PerRef | PerRef |

