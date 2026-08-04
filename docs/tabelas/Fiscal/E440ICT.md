# E440ICT

## Descrição

Compras - Contagens de Produtos - Itens

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCnt | Number(009,0) | Não | Número da contagem |
| SeqCnt | Number(009,0) | Não | Sequência do item na contagem |
| CodPro | String(014) | Sim | Código do produto na contagem |
| CodDer | String(007) | Sim | Código da derivação do produto na contagem |
| QtdCnt | Number(014,5) | Sim | Quantidade contada no recebimento do produto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do item |
| DatGer | Date | Sim | Data da geração do item |
| HorGer | Number(005,0) | Sim | Hora da geração do item |
| ObsIct | String(250) | Sim | Texto da observação |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| QtdDef | Number(014,5) | Sim | Quantidade com defeito no recebimento do produto |

---

## Chave Primária

- CodEmp
- CodFil
- NumCnt
- SeqCnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
