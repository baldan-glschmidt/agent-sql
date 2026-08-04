# E062LOC

## Descrição

Tabelas - Locais de Entrega

---

## Resumo

- Campos: 15
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| LocEnt | Number(008,0) | Não | Código da localização para a entrega das mercadorias |
| DesEnt | String(030) | Sim | Descrição da localização para a entrega das mercadorias |
| KmtTot | Number(008,2) | Sim | Quilometragem total do local de entrega |
| CepOri | Number(008,0) | Sim | CEP Cidade Origem |
| CepDes | Number(008,0) | Sim | CEP Cidade Destino |
| HorRoe | Number(004,0) | Sim | Tempo da Rota em Horas. |
| SitLoc | String(001) | Sim | Situação do local de entrega |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodEmp | Number(004,0) | Sim | Código da empresa na qual pertence a localização |
| CodFil | Number(005,0) | Sim | Código da filial onde pertence a localização |

---

## Chave Primária

- LocEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
