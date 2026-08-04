# E000CGR

## Descrição

Integrações - Controle de Geração de Relatórios

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqCgr | Number(009,0) | Não | Sequencia de geração de relatório |
| SitCgr | String(001) | Não | Situação da geração do relatório |
| DatIni | Date | Sim | Data de início da geração do relatório |
| HorIni | Number(005,0) | Sim | Hora de início de geração do relatório |
| DatFim | Date | Sim | Data do término da geração do relatório |
| HorFim | Number(005,0) | Sim | Hora de término do relatório |
| CodInt | Number(002,0) | Não | Código do sistema integrado |
| NomArq | String(255) | Sim | Nome do Arquivo gerado |
| MsgErr | String(255) | Sim | Mensagem erro do processamento da requisição |

---

## Chave Primária

- SeqCgr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
