# R000IGS

## Descrição

Configurações Integração GED/SIGN

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipAmb | Number(002,0) | Não | Tipo de Ambiente |
| UrlAmb | String(250) | Não | URL |
| Tenant | String(100) | Não | Tenant |
| AccKey | String(150) | Não | Access Key |
| Secret | String(100) | Não | Secret |
| NotEma | String(001) | Sim | Notificação por E-mail |
| NotSms | String(001) | Sim | Notificação por SMS - Obsoleto |
| NotApp | String(001) | Sim | Notificação por WhatsApp |
| NotPla | String(001) | Sim | Notificação pela Plataforma |
| DomCli | String(100) | Sim | Domínio |
| CamGed | String(200) | Sim | Caminho do arquivo no GED |
| AssCol | Number(002,0) | Sim | Ação do colaborador em relação ao documento |
| CodReg | Number(003,0) | Sim | Código da regra executada ao abrir a tela de envio de documento para assinatura |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
