# E062ROE

## Descrição

Tabelas - Rotas ou Localidades de Entrega

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRoe | String(003) | Não | Código da Rota ou Localidade |
| DesRoe | String(030) | Não | Descrição da Rota ou Localidade |
| MaxEnt | Number(004,0) | Sim | Número máximo de entregas no dia |
| KmtTot | Number(008,2) | Sim | Quilometragem total da Rota |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| CepOri | Number(008,0) | Sim | CEP Cidade Origem |
| CepDes | Number(008,0) | Sim | CEP Cidade Destino |
| HorRoe | Number(004,0) | Sim | Tempo da Rota em Horas. |
| CodFor | Number(009,0) | Sim | Código do fornecedor para a rota |
| SitRoe | String(001) | Sim | Situação da rota de entrega |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| VlrAdr | Number(015,2) | Sim | Valor adicional da rota a ser pago ao motorista |

---

## Chave Primária

- CodRoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
