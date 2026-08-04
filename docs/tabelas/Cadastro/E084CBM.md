# E084CBM

## Descrição

Cadastros - Máscara Código do Bem - Componentes

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMbm | String(008) | Não | Código da Máscara do Bem |
| CodMcb | String(014) | Não | Código do Componente da Máscara de Bem |
| DesMcb | String(020) | Não | Descrição do Componente da Máscara |
| AbrMcb | String(010) | Não | Abreviatura do Componente da Máscara |
| CodEsp | Number(004,0) | Sim | Código da espécie do bem |
| CodFil | Number(005,0) | Sim | Código da Filial |

---

## Chave Primária

- CodEmp
- CodMbm
- CodMcb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CBM_001

**Tabela:** E084MBM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMbm | CodMbm |

