# R202PER

## Descrição

Teste Certificação - Perguntas

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruPer | Number(005,0) | Não | Código do teste |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| CunPer | String(001) | Sim | Cunho da Pergunta |
| DesPer | String(4000) | Sim | Descrição da Pergunta |
| PesPer | Number(002,0) | Sim | Peso da Pergunta |
| NotPer | Number(006,2) | Sim | Nota da Pergunta |
| TemRes | Number(003,0) | Sim | Tempo (segundos) para responder o Teste Efetivo |
| TReSim | Number(003,0) | Sim | Tempo (segundos) para responder o Teste Simulado |
| DatCri | Date | Sim | Data de Criação da Pergunta |
| DatExt | Date | Sim | Data de Extinção da Pergunta |
| ConSim | String(001) | Sim | Considera esta pergunta em teste simulado |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência |
| AbrEmp | String(200) | Sim | Abrangência de Empresa |
| AbrFil | String(200) | Sim | Abrangência de filial |
| AbrCar | String(100) | Sim | Abrangência de cargo |
| AbrLoc | String(1500) | Sim | Abrangência de local |
| AbrTur | String(025) | Sim | Abrangência nos Turnos |
| TipACa | String(001) | Sim | Tipo de Abrangência do Campo |

---

## Chave Primária

- GruPer
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R202PER_000

**Tabela:** R202GRU

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |

