# R067LLE

## Descrição

Log Leitura Arquivos de Marcações

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomArq | String(050) | Não | Nome do Arquivo (Após Renomear) |
| DatArq | Date | Não | Data do Arquivo Lido |
| HorArq | Number(005,0) | Não | Hora do Arquivo Lido |
| TamArq | Number(009,0) | Não | Tamanho em Bytes do Arquivo Lido |
| DatLei | Date | Não | Data da Leitura do Arquivo |
| HorLei | Number(009,0) | Não | Hora/Minuto da Leitura do Arquivo |
| NomOAr | String(050) | Sim | Nome Original do Arquivo Lido (Antes de Renomear) |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Realizou a Leitura do Arquivo |
| TotInc | Number(009,0) | Sim | Total de Marcações do Arquivo Incluídas na Base |
| TotRej | Number(009,0) | Sim | Total de Marcações do Arquivo Rejeitadas na Leitura |

---

## Chave Primária

- NomArq
- DatArq
- HorArq
- TamArq
- DatLei
- HorLei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
