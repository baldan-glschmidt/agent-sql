# E084CSL

## Descrição

Cadastros - Máscara Séries e Lotes - Componentes

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMsl | String(008) | Não | Código  da Máscara |
| CodCsl | String(050) | Não | Código do Componente da Máscara |
| SeqCsl | Number(004,0) | Não | Número  Sequencial  dos componentes da máscara |
| DesCsl | String(020) | Não | Descrição do Componente da Máscara |
| AbrCsl | String(010) | Não | Abreviatura do Componente da Máscara |

---

## Chave Primária

- CodEmp
- CodMsl
- CodCsl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CSL_001

**Tabela:** E084MSL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMsl | CodMsl |

