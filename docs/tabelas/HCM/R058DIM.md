# R058DIM

## Descrição

Dimensões do Modelo de Dispositivo

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| UniMed | Number(001,0) | Sim | Unidade de Medida |
| AltMod | Number(006,2) | Sim | Altura do Modelo |
| LarMod | Number(006,2) | Sim | Largura do Modelo |
| ProMod | Number(006,2) | Sim | Profundidade do Modelo |

---

## Chave Primária

- ModRlg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058DIM_000

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

