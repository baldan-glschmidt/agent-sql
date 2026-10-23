# R058MOP

## Descrição

Modelos por Site

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| CodPlt | Number(005,0) | Não | Código do Site |
| DirMar | String(200) | Sim | Diretório dos Arquivos de Marcações do Coletor |
| DirRej | String(200) | Sim | Diretório dos Arquivos das Marcações Rejeitadas |
| MesCol | String(035) | Sim | Registro Mestre dos Arquivos de Marcações do Coletor |
| MarCol | String(100) | Sim | Registro de Marcação dos Arquivos de Marcações do Coletor |

---

## Chave Primária

- ModRlg
- CodPlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058MOP_000

**Tabela:** R058MOD

| Origem | Destino |
|--------|---------|
| ModRlg | ModRlg |

### IR_R058MOP_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

