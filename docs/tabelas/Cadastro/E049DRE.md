# E049DRE

## Descrição

Tabelas - Definição do Registro

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDec | Number(009,0) | Não | Código da declaração |
| CodReg | String(010) | Não | Código do registro da declaração |
| NomCam | String(250) | Não | Nome do campo |
| DesCam | String(250) | Sim | Descrição do campo |
| RefCam | String(250) | Sim | Referência de entrada/saída do campo |
| TipCam | Number(001,0) | Não | Tipo de dado do campo |
| SeqCam | Number(004,0) | Não | Sequência do campo no registro |
| TamCam | Number(006,0) | Sim | Tamanho do campo |
| MscCam | String(025) | Sim | Máscara do campo |
| MscNul | String(025) | Sim | Máscara do campo quando o valor do mesmo estiver branco ou zerado |
| IndKey | String(001) | Sim | Indicativo se o campo pertence a chave do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| CmpLst | String(255) | Sim | Caminho do arquivo da lista com as opções |

---

## Chave Primária

- CodDec
- CodReg
- NomCam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
