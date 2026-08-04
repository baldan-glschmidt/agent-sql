# E084CME

## Descrição

Cadastros - Máscara Endereçamento Produto - Componentes

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
| CodMep | String(008) | Não | Código da máscara endereçamento produto |
| CodCme | String(020) | Não | Código do componente da máscara de endereçamento produto |
| SeqCme | Number(009,0) | Não | Número sequencial  dos componentes da máscara |
| DesCme | String(050) | Não | Descrição do componente da máscara |
| AbrCme | String(020) | Não | Abreviatura do componente da máscara |
| SitCme | String(001) | Não | Situação do componente da máscara de endereçamento produto |

---

## Chave Primária

- CodEmp
- CodMep
- CodCme

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084CME_001

**Tabela:** E084MEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMep | CodMep |

