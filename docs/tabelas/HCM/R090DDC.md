# R090DDC

## Descrição

Definição de Documentos

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDac | Number(003,0) | Não | Código da Definição de Acesso |
| PriSeg | Number(001,0) | Não | Primeiro ou Segundo Documento |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |

---

## Chave Primária

- CodDac
- PriSeg
- TipDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090DDC_000

**Tabela:** R070DAC

| Origem | Destino |
|--------|---------|
| CodDac | CodDac |

