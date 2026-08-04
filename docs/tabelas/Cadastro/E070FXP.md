# E070FXP

## Descrição

Cadastros - Filiais - Produtos não Permitidos

---

## Resumo

- Campos: 14
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqFxp | Number(009,0) | Não | Sequência de produtos que não pode ser enviados para a filial |
| CodOri | String(003) | Sim | Código de Origem do Produto não permitida na filial |
| CodFam | String(006) | Sim | Código da Família do Produto não permitida na filial |
| CodAge | String(005) | Sim | Código do agrupamento de estoques não permitido na filial |
| CodAgc | String(005) | Sim | Código do agrupamento comercial não permitido na filial |
| CodAgg | String(001) | Sim | Código de agrupamento de materiais/produtos para garantia estendida |
| CodPro | String(014) | Sim | Código do produto não permitido na filial |
| CodDer | String(007) | Sim | Código da derivação do produto não permitida na filial |
| ObsFxp | String(250) | Sim | Texto da observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- SeqFxp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
