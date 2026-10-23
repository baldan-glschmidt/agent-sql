# R152PEN

## Descrição

Tabela de Controle de Pendências para Eventos Aduaneiros

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código da pendência de Recintos Aduaneiros |
| TipEve | Number(001,0) | Não | Tipo de evento da pendência de Recintos Aduaneiros |
| TipOpe | String(001) | Não | Tipo da operação do evento |
| DthPen | Date | Não | Data e hora de criação da pendência |
| DthEnv | Date | Sim | Data e hora do envio da pendência para o eDocs |
| DthRet | Date | Sim | Data/Hora do último retorno da pendência pelo eDocs |
| StaPen | Number(001,0) | Não | Status da pendência de Recintos Aduaneiros |
| DthAut | Date | Sim | Data/Hora da autorização do evento retornado com sucesso pelo Portal Siscomex |
| ProTra | String(036) | Sim | Protocolo da transmissão do evento retornado com sucesso pelo Portal Siscomex |
| VerPlf | Number(003,0) | Sim | Versão do plano de localização física do recinto aduaneiro |
| CodPlf | Number(007,0) | Sim | Código do local físico do recinto aduaneiro |
| CodRec | Number(015,0) | Sim | Código do recinto aduaneiro |

---

## Chave Primária

- CodPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
