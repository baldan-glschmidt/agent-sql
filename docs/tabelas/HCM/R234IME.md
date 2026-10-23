# R234IME

## Descrição

Evento - Documentos

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| SeqImg | Number(004,0) | Não | Sequência do Documento |
| DatArq | Date | Sim | Data do Documento |
| Imagem | Image | Sim | Arquivo |
| DesImg | String(060) | Sim | Descrição do Documento |
| NomArq | String(250) | Sim | Nome Arquivo |

---

## Chave Primária

- CodEvn
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234IME_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

