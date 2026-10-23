# R058EME

## Descrição

Prioridade de Execução da Emergência

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| SeqExe | Number(003,0) | Não | Sequência da Execução |
| CodRlg | Number(005,0) | Sim | Código do Coletor |

---

## Chave Primária

- CodPlt
- SeqExe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058EME_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058EME_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

