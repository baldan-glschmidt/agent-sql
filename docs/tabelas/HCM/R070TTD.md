# R070TTD

## Descrição

Tabela Temporária Telemática Dat07/Dat08

---

## Resumo

- Campos: 20
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipTab | Number(001,0) | Sim | Tipo tabela (Dat07/Dat08) |
| NumEip | String(015) | Sim | Número do Endereço IP (END_IP) |
| CodCen | String(002) | Sim | Centralizadora (BLUEB) |
| CodAlf | String(002) | Sim | Código do Coletor Alfa (CODIN) |
| DesRlg | String(030) | Sim | Descrição do Coletor (DESC_END) |
| CodPrm | String(003) | Sim | Código da Permissão (LACES) |
| TipTer | String(001) | Sim | Tipo Terminal (TIP_TERM) |
| CTFuso | String(004) | Sim | Controle Fuso Horário (FUSO) |
| CodPlt | String(005) | Sim | Código site (PLANTA) |
| TipBio | String(001) | Sim | Tipo da leitora biomátrica (BIO_TIPO) |
| TipLei | String(001) | Sim | Tipo de leitora smart card (TIP_LEIT) |
| AtuFor | String(001) | Sim | Atualização forçada (ATUFORC) |
| DatFor | Date | Sim | Data final de atualização forçada (DATFORC) |
| RFIDrt | String(001) | Sim | RFID rastreador (RASTREADOR) |
| ValRet | String(001) | Sim | Validação de interjornada (VALID_RET) |
| IniHal | String(001) | Sim | Validação horário de almoço - início (POS_INIHALM) |
| FimHal | String(001) | Sim | Validação horário de almoço - finalização (POS_FIMHALM) |
| SaiMax | String(001) | Sim | Validação de horário de saída máxima (VALID_SAIDAMAX) |
| FaiPrm | String(056) | Sim | Faixa horária (FXPERM) |
| BloCon | Number(001,0) | Sim | Bloquear conexão com dispositivo |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
