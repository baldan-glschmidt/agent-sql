# R090FOT

## Descrição

Foto de ocorrência na portaria

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| SeqFot | Number(002,0) | Não | Sequência da foto na ocorrência |
| FotOcp | Image | Sim | Foto da ocorrência |
| VerPlf | Number(003,0) | Sim | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Sim | Código do Local Físico |
| CodUsu | Number(010,0) | Sim | Código do Usuário |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP
- SeqFot

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090FOT_003

**Tabela:** R090OCP

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| DatOcP | DatOcP |
| HorOcP | HorOcP |
| SeqOcP | SeqOcP |

