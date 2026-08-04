# E084LOP

## Descrição

Cadastros - Liga Opções da Máscara ao Produto

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMpc | String(008) | Não | Código da Opção da Máscara de Produto |
| CodCpc | String(014) | Não | Código do Componente da Opção da Máscara de Produto |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Derivação do Produto |
| CodUsu | Number(010,0) | Não | Código do Usuário que alterou |
| DatGer | Date | Não | Data Geração ou Alteração da ligação |
| HorGer | Number(005,0) | Não | Hora da geração/última alteração do registro |

---

## Chave Primária

- CodEmp
- CodMpc
- CodCpc
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E084LOP_002

**Tabela:** E084CPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMpc | CodMpc |
| CodCpc | CodCpc |

